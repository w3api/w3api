---
title: SystemResourcePressureMXBean.setMemoryPressure()
permalink: /Java/SystemResourcePressureMXBean/setMemoryPressure/
date: 2021-01-11
key: Java.S.SystemResourcePressureMXBean
category: Java
tags: ['java se', 'jdk.management.cmm', 'jdk.management.cmm', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SystemResourcePressureMXBean.metodos valor="setMemoryPressure" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setMemoryPressure(int pressureLevel)
~~~

## Parámetros
* **int pressureLevel**,  {% include w3api/param_description.html metodo=_dato parametro="int pressureLevel" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SystemResourcePressureMXBean](/Java/SystemResourcePressureMXBean/)

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
