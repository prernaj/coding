#include <iostream>

using namespace std;

struct Vertex {
    int vertexNum;
    struct Vertex* next;
};

class Graph {
    private:
        int numVertices;
        Vertex** adjList;
    public:
        Graph(int numVertices) {
            cout << "constructing graph\n";
            this->numVertices = numVertices;
            adjList = new Vertex*[numVertices];
            // initializatiion
            for (int i = 0; i < numVertices; i++) {
                adjList[i] = new Vertex;
                adjList[i]->vertexNum = i;
                adjList[i]->next = adjList[i];
            }
        }

        void addEdge(int u, int v) {
            cout << "adding edge" << u << " " << v << "\n";
            Vertex* x = new Vertex;
            x->vertexNum = v;
            x->next = adjList[u];
            Vertex* node = adjList[u];
            while(node && node->next->vertexNum != u) {
                node = node->next;
            }
            node->next = x;
        }

        void removeEdge(int u, int v) {
            cout << "removing edge\n";
            Vertex* node = adjList[u];
            while(node && node->next and node->next->vertexNum == v) {
                node = node->next;
            }
            if(node->next) {
                node->next = node->next->next;
            }
        }

        bool isEdge(int u, int v) {
            cout << "is edge\n";
            Vertex* node = adjList[u];
            while(node->next and node->next->vertexNum == v) {
                node = node->next;
            }
            if(node->next) 
                return true;
            return false;
            
        } 

        void printGraph() {
            cout << "printing graph\n";
            for (int u = 0; u < numVertices; u++) {
                cout << u << " : ";
                Vertex* node = adjList[u]->next;
                while(node->vertexNum != u) {
                    cout << node->vertexNum << " ";
                    node = node->next;
                }
                cout << "\n";
            }
        }

        ~Graph() {
            cout << "destructing graph";
            for (int i = 0; i < numVertices; i++) {
                delete[] adjList[i];
            }
            delete[] adjList;
        }
};

int main() {
    Graph g(4);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);

    g.printGraph();
}
