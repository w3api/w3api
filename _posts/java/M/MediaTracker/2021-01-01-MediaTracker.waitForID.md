---
title: MediaTracker.waitForID()
permalink: Java/MediaTracker/waitForID
date: 2021-01-11
key: JavaJava.M.MediaTracker
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaTracker.metodos valor="waitForID" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void waitForID(int id) throws InterruptedException
public boolean waitForID(int id, long ms) throws InterruptedException
~~~

## Parámetros
* **long ms**,  {% include w3api/param_description.html metodo=_dato parametro="long ms" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}

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
