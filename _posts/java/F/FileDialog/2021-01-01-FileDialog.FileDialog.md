---
title: FileDialog.FileDialog()
permalink: Java/FileDialog/FileDialog
date: 2021-01-11
key: JavaJava.F.FileDialog
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileDialog.constructores valor="FileDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileDialog(Dialog parent)
public FileDialog(Dialog parent, String title)
public FileDialog(Dialog parent, String title, int mode)
public FileDialog(Frame parent)
public FileDialog(Frame parent, String title)
public FileDialog(Frame parent, String title, int mode)
~~~

## Parámetros
* **Frame parent**,  {% include w3api/param_description.html metodo=_dato parametro="Frame parent" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Dialog parent**,  {% include w3api/param_description.html metodo=_dato parametro="Dialog parent" %}
* **int mode**,  {% include w3api/param_description.html metodo=_dato parametro="int mode" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FileDialog](/Java/FileDialog/)

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
