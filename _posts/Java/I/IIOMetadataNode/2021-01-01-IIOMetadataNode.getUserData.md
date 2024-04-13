---
title: IIOMetadataNode.getUserData()
permalink: /Java/IIOMetadataNode/getUserData/
date: 2021-01-11
key: Java.I.IIOMetadataNode
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="getUserData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getUserData(String key) throws DOMException
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
