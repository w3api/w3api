---
title: NamespaceContext.getPrefix()
permalink: /Java/NamespaceContext/getPrefix/
date: 2021-01-11
key: Java.N.NamespaceContext
category: Java
tags: ['java se', 'javax.xml.namespace', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamespaceContext.metodos valor="getPrefix" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getPrefix(String namespaceURI)
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
