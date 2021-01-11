---
title: JTabbedPane.setTabComponentAt()
permalink: Java/JTabbedPane/setTabComponentAt
date: 2021-01-11
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setTabComponentAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, description="The tab component at the specified tab index.") public void setTabComponentAt(int index, Component component)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
