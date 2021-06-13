---
title: TimerMBean.removeNotifications()
permalink: /Java/TimerMBean/removeNotifications/
date: 2021-01-11
key: Java.T.TimerMBean
category: Java
tags: ['java se', 'javax.management.timer', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimerMBean.metodos valor="removeNotifications" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotifications(String type) throws InstanceNotFoundException
~~~

## Parámetros
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[TimerMBean](/Java/TimerMBean/)

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
