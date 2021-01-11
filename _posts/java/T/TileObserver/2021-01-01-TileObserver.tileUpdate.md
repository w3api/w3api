---
title: TileObserver.tileUpdate()
permalink: Java/TileObserver/tileUpdate
date: 2021-01-11
key: JavaJava.T.TileObserver
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TileObserver.metodos valor="tileUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void tileUpdate(WritableRenderedImage source, int tileX, int tileY, boolean willBeWritable)
~~~

## Parámetros
* **int tileY**,  {% include w3api/param_description.html metodo=_dato parametro="int tileY" %}
* **int tileX**,  {% include w3api/param_description.html metodo=_dato parametro="int tileX" %}
* **boolean willBeWritable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean willBeWritable" %}
* **WritableRenderedImage source**,  {% include w3api/param_description.html metodo=_dato parametro="WritableRenderedImage source" %}

## Clase Padre
[TileObserver](/Java/TileObserver/)

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
