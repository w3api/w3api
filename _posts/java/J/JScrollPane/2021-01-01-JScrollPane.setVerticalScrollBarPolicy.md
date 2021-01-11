---
title: JScrollPane.setVerticalScrollBarPolicy()
permalink: Java/JScrollPane/setVerticalScrollBarPolicy
date: 2021-01-11
key: JavaJava.J.JScrollPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollPane.metodos valor="setVerticalScrollBarPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, enumerationValues={"ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER","ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS"}, description="The scrollpane vertical scrollbar policy") public void setVerticalScrollBarPolicy(int policy)
~~~

## Parámetros
* **int policy**,  {% include w3api/param_description.html metodo=_dato parametro="int policy" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JScrollPane](/Java/JScrollPane/)

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
