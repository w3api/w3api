---
title: DefaultMutableTreeNode.insert()
permalink: Java/DefaultMutableTreeNode/insert
date: 2021-01-04
key: JavaJava.D.DefaultMutableTreeNode
category: java
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
* **MutableTreeNode newChild**,  {% include w3api/param_description.html metodo=_data parametro="MutableTreeNode newChild" %}
* **int childIndex**,  {% include w3api/param_description.html metodo=_data parametro="int childIndex" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DefaultMutableTreeNode](/Java/DefaultMutableTreeNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultMutableTreeNode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
