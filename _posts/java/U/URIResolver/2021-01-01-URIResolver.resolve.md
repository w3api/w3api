---
title: URIResolver.resolve()
permalink: Java/URIResolver/resolve
date: 2021-01-11
key: JavaJava.U.URIResolver
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URIResolver.metodos valor="resolve" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Source resolve(String href, String base) throws TransformerException
~~~

## Parámetros
* **String base**,  {% include w3api/param_description.html metodo=_dato parametro="String base" %}
* **String href**,  {% include w3api/param_description.html metodo=_dato parametro="String href" %}

## Excepciones
[TransformerException](/Java/TransformerException/)

## Clase Padre
[URIResolver](/Java/URIResolver/)

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
