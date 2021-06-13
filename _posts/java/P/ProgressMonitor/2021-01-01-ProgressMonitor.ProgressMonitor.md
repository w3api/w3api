---
title: ProgressMonitor.ProgressMonitor()
permalink: /Java/ProgressMonitor/ProgressMonitor/
date: 2021-01-11
key: Java.P.ProgressMonitor
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProgressMonitor.constructores valor="ProgressMonitor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProgressMonitor(Component parentComponent, Object message, String note, int min, int max)
~~~

## Parámetros
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}
* **int max**,  {% include w3api/param_description.html metodo=_dato parametro="int max" %}
* **String note**,  {% include w3api/param_description.html metodo=_dato parametro="String note" %}
* **Object message**,  {% include w3api/param_description.html metodo=_dato parametro="Object message" %}
* **int min**,  {% include w3api/param_description.html metodo=_dato parametro="int min" %}

## Clase Padre
[ProgressMonitor](/Java/ProgressMonitor/)

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
