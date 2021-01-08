---
title: FXMLLoader.load()
permalink: Java/FXMLLoader/load
date: 2021-01-04
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
* **Callback&lt;Class&lt;?&gt;**,  {% include w3api/param_description.html metodo=_data parametro="Callback<Class<?>" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **Object&gt; controllerFactory**,  {% include w3api/param_description.html metodo=_data parametro="Object> controllerFactory" %}
* **URL location**,  {% include w3api/param_description.html metodo=_data parametro="URL location" %}
* **BuilderFactory builderFactory**,  {% include w3api/param_description.html metodo=_data parametro="BuilderFactory builderFactory" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inputStream" %}
* **ResourceBundle resources**,  {% include w3api/param_description.html metodo=_data parametro="ResourceBundle resources" %}

## Clase Padre
[FXMLLoader](/Java/FXMLLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FXMLLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
