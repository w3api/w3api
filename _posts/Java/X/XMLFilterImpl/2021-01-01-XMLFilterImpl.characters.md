---
title: XMLFilterImpl.characters()
permalink: /Java/XMLFilterImpl/characters/
date: 2021-01-11
key: Java.X.XMLFilterImpl
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLFilterImpl.metodos valor="characters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void characters(char[] ch, int start, int length) throws SAXException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **char[] ch**,  {% include w3api/param_description.html metodo=_dato parametro="char[] ch" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[XMLFilterImpl](/Java/XMLFilterImpl/)

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
