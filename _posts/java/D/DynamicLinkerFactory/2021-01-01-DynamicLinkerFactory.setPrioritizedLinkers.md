---
title: DynamicLinkerFactory.setPrioritizedLinkers()
permalink: Java/DynamicLinkerFactory/setPrioritizedLinkers
date: 2021-01-11
key: JavaJava.D.DynamicLinkerFactory
category: java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicLinkerFactory.metodos valor="setPrioritizedLinkers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPrioritizedLinkers(List<? extends GuardingDynamicLinker> prioritizedLinkers)
public void setPrioritizedLinkers(GuardingDynamicLinker... prioritizedLinkers)
~~~

## Parámetros
* **GuardingDynamicLinker... prioritizedLinkers**,  {% include w3api/param_description.html metodo=_dato parametro="GuardingDynamicLinker... prioritizedLinkers" %}
* **List&lt;? extends GuardingDynamicLinker&gt; prioritizedLinkers**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends GuardingDynamicLinker> prioritizedLinkers" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DynamicLinkerFactory](/Java/DynamicLinkerFactory/)

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