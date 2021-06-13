---
title: DefaultMutableTreeNode.insert()
permalink: /Java/DefaultMutableTreeNode/insert/
date: 2021-01-11
key: Java.D.DefaultMutableTreeNode
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultMutableTreeNode.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insert(MutableTreeNode newChild, int childIndex)
~~~

## Parámetros
* **MutableTreeNode newChild**,  {% include w3api/param_description.html metodo=_dato parametro="MutableTreeNode newChild" %}
* **int childIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int childIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

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
