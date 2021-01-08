---
title: ThreadMXBean.setThreadCpuTimeEnabled()
permalink: Java/ThreadMXBean-java-lang-management/setThreadCpuTimeEnabled
date: 2021-01-04
key: JavaJava.T.ThreadMXBean-java-lang-management
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-java-lang-management.metodos valor="setThreadCpuTimeEnabled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setThreadCpuTimeEnabled(boolean enable)
~~~

## Parámetros
* **boolean enable**,  {% include w3api/param_description.html metodo=_data parametro="boolean enable" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ThreadMXBean](/Java/ThreadMXBean-java-lang-management/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadMXBean-java-lang-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
