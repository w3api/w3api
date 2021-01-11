---
title: IIOMetadataNode.insertBefore()
permalink: Java/IIOMetadataNode/insertBefore
date: 2021-01-11
key: JavaJava.I.IIOMetadataNode
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="insertBefore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Node insertBefore(Node newChild, Node refChild)
~~~

## Parámetros
* **Node refChild**,  {% include w3api/param_description.html metodo=_dato parametro="Node refChild" %}
* **Node newChild**,  {% include w3api/param_description.html metodo=_dato parametro="Node newChild" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

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
