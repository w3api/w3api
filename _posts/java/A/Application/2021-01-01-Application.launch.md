---
title: Application.launch()
permalink: Java/Application/launch
date: 2021-01-11
key: JavaJava.A.Application
category: java
tags: ['java se', 'javafx.application', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Application.metodos valor="launch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void launch(Class<? extends Application> appClass, String... args)
public static void launch(String... args)
~~~

## Parámetros
* **String... args**,  {% include w3api/param_description.html metodo=_dato parametro="String... args" %}
* **Class&lt;? extends Application&gt; appClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Application> appClass" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[Application](/Java/Application/)

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
