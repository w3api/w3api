---
title: MediaTracker.waitForAll()
permalink: Java/MediaTracker/waitForAll
date: 2021-01-11
key: JavaJava.M.MediaTracker
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaTracker.metodos valor="waitForAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void waitForAll() throws InterruptedException
public boolean waitForAll(long ms) throws InterruptedException
~~~

## Parámetros
* **long ms**,  {% include w3api/param_description.html metodo=_dato parametro="long ms" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[MediaTracker](/Java/MediaTracker/)

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
