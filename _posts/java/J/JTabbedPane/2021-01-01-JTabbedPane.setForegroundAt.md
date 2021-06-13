---
title: JTabbedPane.setForegroundAt()
permalink: /Java/JTabbedPane/setForegroundAt/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setForegroundAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, description="The foreground color at the specified tab index.") public void setForegroundAt(int index, Color foreground)
~~~

## Parámetros
* **Color foreground**,  {% include w3api/param_description.html metodo=_dato parametro="Color foreground" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
