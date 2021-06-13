---
title: NamespaceContext.getPrefixes()
permalink: Java/NamespaceContext/getPrefixes
date: 2021-01-11
key: JavaJava.N.NamespaceContext
category: Java
tags: ['java se', 'javax.xml.namespace', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamespaceContext.metodos valor="getPrefixes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterator<String> getPrefixes(String namespaceURI)
~~~

## Parámetros
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NamespaceContext](/Java/NamespaceContext/)

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
