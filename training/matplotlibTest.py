import numpy as np

def main():
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi,np.pi,360,endpoint=True)
    # c,s = np.cos(x),np.sin(x)
    c = np.cos(x)
    s = np.sin(x)
    plt.figure(2)
    plt.plot(x,c,color = 'blue', linewidth = 1.0, linestyle = '-', label = 'COS', alpha=0.5)
    plt.plot(x,s, 'g*', label = 'SIN')
    plt.title('Cos & Sin')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data',0))
    ax.spines['bottom'].set_position(('data',0))


    plt.show()

if __name__ == '__main__':
     main()