---
title: FXMLLoader.loadType()
permalink: Java/FXMLLoader/loadType
date: 2021-01-04
key: JavaJava.F.FXMLLoader
category: java
tags: ['java se', 'javafx.fxml', 'javafx.fxml', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXMLLoader.metodos valor="loadType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static Class<?> loadType(String className) throws ClassNotFoundException
@Deprecated public static Class<?> loadType(String packageName, String className) throws ClassNotFoundException
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_data parametro="String packageName" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

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
