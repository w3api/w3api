---
title: JEditorPane.setPage()
permalink: Java/JEditorPane/setPage
date: 2021-01-11
key: JavaJava.J.JEditorPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JEditorPane.metodos valor="setPage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPage(String url) throws IOException
@BeanProperty(expert=true, description="the URL used to set content") public void setPage(URL page) throws IOException
~~~

## Parámetros
* **String url**,  {% include w3api/param_description.html metodo=_dato parametro="String url" %}
* **URL page**,  {% include w3api/param_description.html metodo=_dato parametro="URL page" %}

## Excepciones
[IOException](/Java/IOException/)

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
