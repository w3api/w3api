---
title: Background.Background()
permalink: Java/Background/Background
date: 2021-01-04
key: JavaJava.B.Background
category: java
tags: ['java se', 'javafx.scene.layout', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.Background.constructores valor="Background" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Background(List<BackgroundFill> fills, List<BackgroundImage> images)
public Background(BackgroundFill... fills)
public Background(BackgroundFill[] fills, BackgroundImage[] images)
public Background(BackgroundImage... images)
~~~

## Parámetros
* **List&lt;BackgroundImage&gt; images**,  {% include w3api/param_description.html metodo=_data parametro="List<BackgroundImage> images" %}
* **List&lt;BackgroundFill&gt; fills**,  {% include w3api/param_description.html metodo=_data parametro="List<BackgroundFill> fills" %}
* **BackgroundFill... fills**,  {% include w3api/param_description.html metodo=_data parametro="BackgroundFill... fills" %}
* **BackgroundImage[] images**,  {% include w3api/param_description.html metodo=_data parametro="BackgroundImage[] images" %}
* **BackgroundImage... images**,  {% include w3api/param_description.html metodo=_data parametro="BackgroundImage... images" %}
* **BackgroundFill[] fills**,  {% include w3api/param_description.html metodo=_data parametro="BackgroundFill[] fills" %}

## Clase Padre
[Background](/Java/Background/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.Background.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
