---
title: PersistenceService.getNames()
permalink: /Java/PersistenceService/getNames/
date: 2021-01-11
key: Java.P.PersistenceService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceService.metodos valor="getNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String[] getNames(URL url) throws MalformedURLException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}

## Excepciones
[MalformedURLException](/Java/MalformedURLException/), [IOException](/Java/IOException/)

## Clase Padre
[PersistenceService](/Java/PersistenceService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
