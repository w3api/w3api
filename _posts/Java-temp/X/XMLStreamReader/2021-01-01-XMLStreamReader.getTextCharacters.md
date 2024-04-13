---
title: XMLStreamReader.getTextCharacters()
permalink: /Java/XMLStreamReader/getTextCharacters/
date: 2021-01-11
key: Java.X.XMLStreamReader
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamReader.metodos valor="getTextCharacters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
char[] getTextCharacters()
int getTextCharacters(int sourceStart, char[] target, int targetStart, int length) throws XMLStreamException
~~~

## Parámetros
* **char[] target**,  {% include w3api/param_description.html metodo=_dato parametro="char[] target" %}
* **int sourceStart**,  {% include w3api/param_description.html metodo=_dato parametro="int sourceStart" %}
* **int targetStart**,  {% include w3api/param_description.html metodo=_dato parametro="int targetStart" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLStreamReader](/Java/XMLStreamReader/)

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
