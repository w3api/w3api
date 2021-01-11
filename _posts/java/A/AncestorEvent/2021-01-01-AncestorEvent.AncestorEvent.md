---
title: AncestorEvent.AncestorEvent()
permalink: Java/AncestorEvent/AncestorEvent
date: 2021-01-11
key: JavaJava.A.AncestorEvent
category: java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AncestorEvent.constructores valor="AncestorEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AncestorEvent(JComponent source, int id, Container ancestor, Container ancestorParent)
~~~

## Parámetros
* **Container ancestor**,  {% include w3api/param_description.html metodo=_dato parametro="Container ancestor" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Container ancestorParent**,  {% include w3api/param_description.html metodo=_dato parametro="Container ancestorParent" %}
* **JComponent source**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent source" %}

## Clase Padre
[AncestorEvent](/Java/AncestorEvent/)

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
