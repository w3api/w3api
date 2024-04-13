---
title: DefaultMutableTreeNode.remove()
permalink: /Java/DefaultMutableTreeNode/remove/
date: 2021-01-11
key: Java.D.DefaultMutableTreeNode
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultMutableTreeNode.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(int childIndex)
public void remove(MutableTreeNode aChild)
~~~

## Parámetros
* **MutableTreeNode aChild**,  {% include w3api/param_description.html metodo=_dato parametro="MutableTreeNode aChild" %}
* **int childIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int childIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[DefaultMutableTreeNode](/Java/DefaultMutableTreeNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
