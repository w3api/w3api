---
title: ProxySelector.select()
permalink: Java/ProxySelector/select
date: 2021-01-04
key: JavaJava.P.ProxySelector
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProxySelector.metodos valor="select" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract List<Proxy> select(URI uri)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ProxySelector](/Java/ProxySelector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProxySelector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
