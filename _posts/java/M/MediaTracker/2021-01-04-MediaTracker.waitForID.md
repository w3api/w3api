---
title: MediaTracker.waitForID()
permalink: Java/MediaTracker/waitForID
date: 2021-01-04
key: JavaJava.M.MediaTracker
category: java
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
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **long ms**,  {% include w3api/param_description.html metodo=_data parametro="long ms" %}

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
{%- for _ldc in site.data.Java.M.MediaTracker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
