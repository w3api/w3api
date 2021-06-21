---
title: PersistenceService.get()
permalink: /Java/PersistenceService/get/
date: 2021-01-11
key: Java.P.PersistenceService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceService.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents get(URL url) throws MalformedURLException, IOException, FileNotFoundException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [MalformedURLException](/Java/MalformedURLException/), [IOException](/Java/IOException/)

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
