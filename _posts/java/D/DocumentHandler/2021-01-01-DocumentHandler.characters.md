---
title: DocumentHandler.characters()
permalink: /Java/DocumentHandler/characters/
date: 2021-01-11
key: Java.D.DocumentHandler
category: Java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentHandler.metodos valor="characters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void characters(char[] ch, int start, int length) throws SAXException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **char[] ch**,  {% include w3api/param_description.html metodo=_dato parametro="char[] ch" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DocumentHandler](/Java/DocumentHandler/)

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
