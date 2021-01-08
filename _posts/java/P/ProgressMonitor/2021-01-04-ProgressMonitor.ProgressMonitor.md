---
title: ProgressMonitor.ProgressMonitor()
permalink: Java/ProgressMonitor/ProgressMonitor
date: 2021-01-04
key: JavaJava.P.ProgressMonitor
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
* **String note**,  {% include w3api/param_description.html metodo=_data parametro="String note" %}
* **Object message**,  {% include w3api/param_description.html metodo=_data parametro="Object message" %}
* **int max**,  {% include w3api/param_description.html metodo=_data parametro="int max" %}
* **int min**,  {% include w3api/param_description.html metodo=_data parametro="int min" %}
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_data parametro="Component parentComponent" %}

## Clase Padre
[ProgressMonitor](/Java/ProgressMonitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProgressMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
