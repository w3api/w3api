---
title: RMIConnection.removeNotificationListeners()
permalink: Java/RMIConnection/removeNotificationListeners
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="removeNotificationListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotificationListeners(ObjectName name, Integer[] listenerIDs, Subject delegationSubject) throws InstanceNotFoundException, ListenerNotFoundException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **Integer[] listenerIDs**,  {% include w3api/param_description.html metodo=_dato parametro="Integer[] listenerIDs" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [ListenerNotFoundException](/Java/ListenerNotFoundException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
