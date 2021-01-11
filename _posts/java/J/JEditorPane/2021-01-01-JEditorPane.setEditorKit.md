---
title: JEditorPane.setEditorKit()
permalink: Java/JEditorPane/setEditorKit
date: 2021-01-11
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="setEditorKit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, description="the currently installed kit for handling content") public void setEditorKit(EditorKit kit)
~~~

## Parámetros
* **EditorKit kit**,  {% include w3api/param_description.html metodo=_dato parametro="EditorKit kit" %}

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
