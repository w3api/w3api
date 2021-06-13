---
title: Application.start()
permalink: /Java/Application/start/
date: 2021-01-11
key: Java.A.Application
category: Java
tags: ['java se', 'javafx.application', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Application.metodos valor="start" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void start(Stage primaryStage) throws Exception
~~~

## Parámetros
* **Stage primaryStage**,  {% include w3api/param_description.html metodo=_dato parametro="Stage primaryStage" %}

## Excepciones
[Exception](/Java/Exception/)

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
