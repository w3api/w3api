---
title: LexicalHandler.startEntity()
permalink: Java/LexicalHandler/startEntity
date: 2021-01-04
key: JavaJava.L.LexicalHandler
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0 (extensions Java 1.0)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LexicalHandler.metodos valor="startEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void startEntity(String name) throws SAXException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[LexicalHandler](/Java/LexicalHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LexicalHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
