---
title: JEditorPane.setContentType()
permalink: Java/JEditorPane/setContentType
date: 2021-01-11
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="setContentType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, description="the type of content") public final void setContentType(String type)
~~~

## Parámetros
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JEditorPane](/Java/JEditorPane/)

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
