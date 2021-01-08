---
title: JobStateReasons.JobStateReasons()
permalink: Java/JobStateReasons/JobStateReasons
date: 2021-01-04
key: JavaJava.J.JobStateReasons
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JobStateReasons.constructores valor="JobStateReasons" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JobStateReasons()
public JobStateReasons(int initialCapacity)
public JobStateReasons(int initialCapacity, float loadFactor)
public JobStateReasons(Collection<JobStateReason> collection)
~~~

## Parámetros
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}
* **Collection&lt;JobStateReason&gt; collection**,  {% include w3api/param_description.html metodo=_data parametro="Collection<JobStateReason> collection" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JobStateReasons](/Java/JobStateReasons/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JobStateReasons.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
