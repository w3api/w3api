---
title: JScrollPane.setHorizontalScrollBarPolicy()
permalink: Java/JScrollPane/setHorizontalScrollBarPolicy
date: 2021-01-11
key: JavaJava.J.JScrollPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollPane.metodos valor="setHorizontalScrollBarPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, enumerationValues={"ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER","ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS"}, description="The scrollpane scrollbar policy") public void setHorizontalScrollBarPolicy(int policy)
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
