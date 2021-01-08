---
title: TileObserver.tileUpdate()
permalink: Java/TileObserver/tileUpdate
date: 2021-01-04
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
* **int tileX**,  {% include w3api/param_description.html metodo=_data parametro="int tileX" %}
* **int tileY**,  {% include w3api/param_description.html metodo=_data parametro="int tileY" %}
* **WritableRenderedImage source**,  {% include w3api/param_description.html metodo=_data parametro="WritableRenderedImage source" %}
* **boolean willBeWritable**,  {% include w3api/param_description.html metodo=_data parametro="boolean willBeWritable" %}

## Clase Padre
[TileObserver](/Java/TileObserver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TileObserver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
