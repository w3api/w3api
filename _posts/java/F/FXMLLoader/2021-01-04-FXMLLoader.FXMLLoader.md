---
title: FXMLLoader.FXMLLoader()
permalink: Java/FXMLLoader/FXMLLoader
date: 2021-01-04
key: JavaJava.F.FXMLLoader
category: java
tags: ['java se', 'javafx.fxml', 'javafx.fxml', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXMLLoader.constructores valor="FXMLLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FXMLLoader()
public FXMLLoader(URL location)
public FXMLLoader(URL location, ResourceBundle resources)
public FXMLLoader(URL location, ResourceBundle resources, BuilderFactory builderFactory)
public FXMLLoader(URL location, ResourceBundle resources, BuilderFactory builderFactory, Callback<Class<?>,Object> controllerFactory)
public FXMLLoader(URL location, ResourceBundle resources, BuilderFactory builderFactory, Callback<Class<?>,Object> controllerFactory, Charset charset)
public FXMLLoader(URL location, ResourceBundle resources, BuilderFactory builderFactory, Callback<Class<?>,Object> controllerFactory, Charset charset, LinkedList<FXMLLoader> loaders)
public FXMLLoader(Charset charset)
~~~

## Parámetros
* **Callback&lt;Class&lt;?&gt;**,  {% include w3api/param_description.html metodo=_data parametro="Callback<Class<?>" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **Object&gt; controllerFactory**,  {% include w3api/param_description.html metodo=_data parametro="Object> controllerFactory" %}
* **URL location**,  {% include w3api/param_description.html metodo=_data parametro="URL location" %}
* **BuilderFactory builderFactory**,  {% include w3api/param_description.html metodo=_data parametro="BuilderFactory builderFactory" %}
* **LinkedList&lt;FXMLLoader&gt; loaders**,  {% include w3api/param_description.html metodo=_data parametro="LinkedList<FXMLLoader> loaders" %}
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
