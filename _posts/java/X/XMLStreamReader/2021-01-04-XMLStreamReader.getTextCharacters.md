---
title: XMLStreamReader.getTextCharacters()
permalink: Java/XMLStreamReader/getTextCharacters
date: 2021-01-04
key: JavaJava.X.XMLStreamReader
category: java
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **char[] target**,  {% include w3api/param_description.html metodo=_data parametro="char[] target" %}
* **int targetStart**,  {% include w3api/param_description.html metodo=_data parametro="int targetStart" %}
* **int sourceStart**,  {% include w3api/param_description.html metodo=_data parametro="int sourceStart" %}

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
{%- for _ldc in site.data.Java.X.XMLStreamReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
