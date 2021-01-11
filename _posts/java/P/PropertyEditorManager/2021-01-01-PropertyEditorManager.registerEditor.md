---
title: PropertyEditorManager.registerEditor()
permalink: Java/PropertyEditorManager/registerEditor
date: 2021-01-11
key: JavaJava.P.PropertyEditorManager
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyEditorManager.metodos valor="registerEditor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void registerEditor(Class<?> targetType, Class<?> editorClass)
~~~

## Parámetros
* **Class&lt;?&gt; editorClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> editorClass" %}
* **Class&lt;?&gt; targetType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> targetType" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[PropertyEditorManager](/Java/PropertyEditorManager/)

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
