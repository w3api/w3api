---
title: IIOMetadataNode.replaceChild()
permalink: Java/IIOMetadataNode/replaceChild
date: 2021-01-04
key: JavaJava.I.IIOMetadataNode
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="replaceChild" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Node replaceChild(Node newChild, Node oldChild)
~~~

## Parámetros
* **Node newChild**,  {% include w3api/param_description.html metodo=_data parametro="Node newChild" %}
* **Node oldChild**,  {% include w3api/param_description.html metodo=_data parametro="Node oldChild" %}

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
{%- for _ldc in site.data.Java.I.IIOMetadataNode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
