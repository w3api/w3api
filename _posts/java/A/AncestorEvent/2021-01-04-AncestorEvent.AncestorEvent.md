---
title: AncestorEvent.AncestorEvent()
permalink: Java/AncestorEvent/AncestorEvent
date: 2021-01-04
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
* **JComponent source**,  {% include w3api/param_description.html metodo=_data parametro="JComponent source" %}
* **Container ancestor**,  {% include w3api/param_description.html metodo=_data parametro="Container ancestor" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **Container ancestorParent**,  {% include w3api/param_description.html metodo=_data parametro="Container ancestorParent" %}

## Clase Padre
[AncestorEvent](/Java/AncestorEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AncestorEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
