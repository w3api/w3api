---
title: URIResolver.resolve()
permalink: Java/URIResolver/resolve
date: 2021-01-04
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
* **String href**,  {% include w3api/param_description.html metodo=_data parametro="String href" %}
* **String base**,  {% include w3api/param_description.html metodo=_data parametro="String base" %}

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
{%- for _ldc in site.data.Java.U.URIResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
