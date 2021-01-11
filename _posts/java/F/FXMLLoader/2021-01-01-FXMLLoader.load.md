---
title: FXMLLoader.load()
permalink: Java/FXMLLoader/load
date: 2021-01-11
key: JavaJava.F.FXMLLoader
category: java
tags: ['java se', 'javafx.fxml', 'javafx.fxml', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXMLLoader.metodos valor="load" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T load()
<T> T load(InputStream inputStream)
static <T> T load(URL location)
static <T> T load(URL location, ResourceBundle resources)
static <T> T load(URL location, ResourceBundle resources, BuilderFactory builderFactory)
static <T> T load(URL location, ResourceBundle resources, BuilderFactory builderFactory, Callback<Class<?>,Object> controllerFactory)
static <T> T load(URL location, ResourceBundle resources, BuilderFactory builderFactory, Callback<Class<?>,Object> controllerFactory, Charset charset)
~~~

## Parámetros
* **ResourceBundle resources**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceBundle resources" %}
* **Object&gt; controllerFactory**,  {% include w3api/param_description.html metodo=_dato parametro="Object> controllerFactory" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **Callback&lt;Class&lt;?&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<Class<?>" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inputStream" %}
* **BuilderFactory builderFactory**,  {% include w3api/param_description.html metodo=_dato parametro="BuilderFactory builderFactory" %}
* **URL location**,  {% include w3api/param_description.html metodo=_dato parametro="URL location" %}

## Clase Padre
[FXMLLoader](/Java/FXMLLoader/)

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
