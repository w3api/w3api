---
title: JTabbedPane.setToolTipTextAt()
permalink: Java/JTabbedPane/setToolTipTextAt
date: 2021-01-11
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setToolTipTextAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The tooltip text at the specified tab index.") public void setToolTipTextAt(int index, String toolTipText)
~~~

## Parámetros
* **String toolTipText**,  {% include w3api/param_description.html metodo=_dato parametro="String toolTipText" %}
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
