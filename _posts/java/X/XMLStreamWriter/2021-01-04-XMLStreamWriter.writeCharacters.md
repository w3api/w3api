---
title: XMLStreamWriter.writeCharacters()
permalink: Java/XMLStreamWriter/writeCharacters
date: 2021-01-04
key: JavaJava.X.XMLStreamWriter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamWriter.metodos valor="writeCharacters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeCharacters(char[] text, int start, int len) throws XMLStreamException
void writeCharacters(String text) throws XMLStreamException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **char[] text**,  {% include w3api/param_description.html metodo=_data parametro="char[] text" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLStreamWriter](/Java/XMLStreamWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLStreamWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
